#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
利用高德地图api实现地址和经纬度的转换
'''
import math
import requests


class Position:
        def __init__(self):
                self.longitude = 0  # 经度
                self.latitude = 0  # 纬度
        def getX(self):
                return self.latitude
        def getY(self):
                return self.longitude
        def setX(self, latitude):
                self.latitude=float(latitude)
        def setY(self, longitude):
                self.longitude=float(longitude)
        def parsePosition(self, str):
                self.longitude = float(str.split(",")[0])
                self.latitude = float(str.split(",")[1])
                return self

        def __str__(self) -> str:
                return "Position{x="+str(self.getX())+", y="+str(self.getY())+"}"


class GaoDeApi:
        def __init__(self):
                KEY="c450fc18e8898cb0c23cfac348a29a65"
                URL_CODE="http://restapi.amap.com/v3/geocode/geo"
                URL_MAP="http://restapi.amap.com/v3/staticmap"

        def geocode(self, address):
                parameters = {'address': address, 'key': self.KEY}
                response = requests.get(self.URL_CODE, parameters)
                answer = response.json()
                # print("answer=", answer)
                return answer

        def map(self, position):
                marks="small,0xFF0000:"+position.getX+","+position.getY()
                parameters = {'markers': marks, 'key': self.KEY}
                response = requests.get(URL_CODE, parameters)
                answer = response.json()
                # print("answer=", answer)
                return answer

        def getLocation(self, address):
                answer = self.geocode(address=address)
                if int(answer['infocode'])==10000:
                        return answer['geocodes'][0]['location']
                else: return "0,0"

        def getPosition(self, address):
                location=self.getLocation(address=address)
                position=Position()
                position=position.parsePosition(location)
                return position

        def isInRange(self, target_position=Position(), range=0, position=Position()):
                # print("tarP=", target_position)
                x_range=range*111*1000
                # print("x_range=", x_range)
                if (position.getX()<= target_position.getX()+x_range)&(position.getX()>=target_position.getX()-x_range):
                        y_range=range * 111 * 1000 * math.cos(position.getX() * math.pi / 180)
                        # print("y_range=", y_range)
                        if (position.getY()<=target_position.getY()+y_range) & (position.getY()>=target_position.getY()-y_range):
                                return True
                return False

