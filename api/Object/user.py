import time

class client:
    def __init__(self, id, profile_id = None):
        self.id = str(id)
        self.profile_id = str(profile_id)
        self.electrode = {"update" : int(time.time())}
        self.data = {"update" : int(time.time())}
        self.time = int(time.time())

    def create(self):
        return [True, {"id": self.id}]

    def loadsave(self, profile_id):
        self.profile_id = str(profile_id)
        return [False, "Can't find user " + str(profile_id) + " in the data base", 404]

    def infos(self):
        return [True, {
            "user_id": self.id,
            "profile_id": self.profile_id,
            "electrodes": self.electrode,
            "data": self.data,
            "time": self.time
        }, 200]

    def changepower(self, id_ele, pow):
        pow = int(pow)
        pow = 100 if pow > 100 else 0 if pow < 0 else pow
        self.electrode[str(id_ele)] = pow
        self.electrode["update"] = int(time.time())
        return [True, [], None]

    def setdata(self, data_id, data):
        self.data[str(data_id)] = int(data)
        self.data["update"] = int(time.time())
        return [True, [], None]
