import base64
import os
def main(args):
      name = args.get("name", "stranger")
      greeting = "Hello " + name + "!"
      cwd = os.curdir
      list = os.listdir(os.curdir + "/assets")

      file = open("./assets/data.xlsx", 'rb')
      file = file.read()
      b64 = base64.b64encode(file).decode('utf-8')
      body = {"b64": b64, 'name': 'badray.png', "len": len(b64)}
      return {"body": body}


# print(main({"name": "badray"}))