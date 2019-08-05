from Model.basic import check, auth
from Object.user import client

USERS = {}

def getauth(cn, nextc):
    err = check.contain(cn.pr, ["pass"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]
    err = [True, auth.gettoken(cn.pr["pass"])]
    return cn.call_next(nextc, err)

def auth(cn, nextc):
    err = check.contain(cn.pr, ["token"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]
    err = auth.verify(cn.pr["token"])
    return cn.call_next(nextc, err)

def create(cn, nextc):
    err = check.contain(cn.pr, ["id"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    use = client(cn.pr["id"])
    err = [True, [], None]
    USERS[str(cn.pr["id"])] = use
    return cn.call_next(nextc, err)

def exist(cn, nextc):
    err = check.contain(cn.pr, ["id"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    err = check.contain(USERS, [str(cn.pr["id"])])
    if not err[0]:
        return cn.toret.add_error("Invalid id: " + str(cn.pr["id"]), 404)
    return cn.call_next(nextc, [True, None, None])

def infos(cn, nextc):
    err = check.contain(cn.pr, ["id"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]
    err = USERS[str(cn.pr["id"])].infos()
    return cn.call_next(nextc, err)

def changepow(cn, nextc):
    err = check.contain(cn.pr, ["id", "index", "value"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]
    err = USERS[str(cn.pr["id"])].changepower(cn.pr["index"], cn.pr["value"])
    return cn.call_next(nextc, err)

def changedata(cn, nextc):
    err = check.contain(cn.pr, ["id", "index", "value"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]
    err = USERS[str(cn.pr["id"])].setdata(cn.pr["index"], cn.pr["value"])
    return cn.call_next(nextc, err)

def allinfos(cn, nextc):
    err = [True, {"users": []}, 200]
    for i in USERS:
        err[1]["users"].append(USERS[str(i)].infos()[1])
    return cn.call_next(nextc, err)
