import json
import os


class ExifInfo:
    def __init__(self, exif):
        """init"""
        if 'Make' in exif.keys():
            self.make = exif['Make']                            # Manufacturer
        else:
            self.make = str()
        if 'Model' in exif.keys():
            self.model = exif['Model']                          # Model
        else:
            self.model = str()
        if 'DateTimeOriginal' in exif.keys():
            self.date_time = exif['DateTimeOriginal']           # DateTime
        else:
            self.date_time = str()
        if 'ISOSpeedRatings' in exif.keys():
            self.iso_speed = exif['ISOSpeedRatings']            # ISO Speed
        else:
            self.iso_speed = int()
        if 'ColorSpace' in exif.keys():
            self.color_space = exif['ColorSpace']               # Color Space
        else:
            self.color_space = int()
        if 'GPSInfo' in exif.keys():
            self.gps = exif['GPSInfo']                          # GPS Info
            self.lat = float()
            self.lng = float()
        else:
            self.gps = dict()
            self.lat = float()
            self.lng = float()
        if 'Orientation' in exif.keys():
            self.orientation = exif['Orientation']              # Direction of Rotation
        else:
            self.orientation = int()
        if 'FocalLength' in exif.keys():
            self.focal_length = exif['FocalLength']             # Focus Length
        else:
            self.focal_length = tuple()
        if 'Flash' in exif.keys():
            self.flash = exif['Flash']                          # Flash
        else:
            self.flash = int()

    def cal_gps(self):
        """calculate GPS Info"""
        if self.gps == dict():
            return

        lat_data = self.gps[2]
        lng_data = self.gps[4]

        """Calculate Latitude, Longitude"""
        lat_deg = lat_data[0][0] / float(lat_data[0][1])
        lat_min = lat_data[1][0] / float(lat_data[1][1])
        lat_sec = lat_data[2][0] / float(lat_data[2][1])

        lng_deg = lng_data[0][0] / float(lng_data[0][1])
        lng_min = lng_data[1][0] / float(lng_data[1][1])
        lng_sec = lng_data[2][0] / float(lng_data[2][1])

        """Set Latitude, Longitude base on N/E/W/S """
        self.lat = (lat_deg + (lat_min + lat_sec / 60.00) / 60.00)

        if self.gps[1] == 'S':
            self.lat *= -1

        self.lng = (lng_deg + (lng_min + lng_sec / 60.00) / 60.00)

        if self.gps[3] == 'W':
            self.lng *= -1

    def cal_focal(self):
        """calculate focal length"""
        plane_x_size = self.focal_length[0]
        plane_y_size = self.focal_length[1]

        self.focal_length = plane_x_size / plane_y_size

    def cal_flash(self):
        """calculate flash value"""
        with open(os.getcwd() + '/analy/core/flash_data.json') as json_data:
            flash_values = json.load(json_data)

        val = str(self.flash)

        if val in flash_values.keys():
            self.flash = flash_values[val]

    def cal_orientation(self):
        """calculate orientation value"""
        with open(os.getcwd() + '/analy/core/orientation_data.json') as json_data:
            ott_value = json.load(json_data)

        val = str(self.orientation)

        if val in ott_value.keys():
            self.orientation = ott_value[val]

    def cal_space(self):
        """calculate color space value"""
        with open(os.getcwd() + "/analy/core/space_data.json") as json_data:
            cs_data = json.load(json_data)

        val = str(self.color_space)

        if val in cs_data.keys():
            self.color_space = cs_data[val]

    def calculate_all(self):
        self.cal_gps()
        self.cal_focal()
        self.cal_flash()
        self.cal_orientation()
        self.cal_space()
