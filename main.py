from flask import Flask, render_template
import pandas as pd
app=Flask(__name__) #Creating website object


#connect HTML Pages with this object
@app.route('/')  #when this website is called with / home function will be executed
def home():
    return render_template('weatherapi.html')

@app.route('/api/v1/<station>/<date>')
def station(station, date):
    filename ="TG_STAID"+str(station).zfill(6)+".txt"
    df=pd.read_csv(filename,skiprows=20,parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE']==date]['   TG'].squeeze()/10

    return {"station": station, "date": date,"temperature":str(temperature)}


if __name__ == '__main__':
    app.run(debug=True,port=5001)