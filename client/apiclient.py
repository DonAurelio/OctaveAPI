#!env/bin/python3
import requests

if __name__ == '__main__':
    file = open('GO003.001','r')
    lines = file.readlines()
    data = list(map(lambda x: float(x),lines))
    r = requests.post('http://localhost:8000/rspectrum/',data = {'x':data})
    print(r)