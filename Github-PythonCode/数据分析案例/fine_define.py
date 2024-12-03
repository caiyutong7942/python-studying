from data_define import Record
import json

class FileReader:

    def read_data(self) ->list[Record]:
        """读取文件的数据，读到的每一条数据都转换为Record对象，将它们都封装到list内返回即可"""
        pass

class TextFileReader(FileReader):

    def __init__(self,path):
        self.path = path

    def read_data(self) ->list[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0],data_list[1],data_list[2],data_list[3])
            record_list.append(record)

        f.close()
        return record_list
    
class JsonFileReader(FileReader):
    
    def __init__(self,path):
        self.path = path

    def read_data(self) ->list[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"],data_dict["order_id"],data_dict["money"],data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list

if __name__ == '__main__':
    txt = TextFileReader("c:\\2011年1月销售数据.txt")
    json1 = JsonFileReader("c:\\2011年2月销售数据JSON.txt")

    txtlist= txt.read_data()
    json1list = json1.read_data()
    
    for l in txtlist:
        print(l)
    for l in json1list:
        print(l)