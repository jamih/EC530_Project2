from pickle import APPENDS
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# names = {"tim": {"age": 19, "gender": "male"},
#  "bill": {"age": 70, "gender": "male"}}

videos = {}

# class HelloWorld(Resource):
#     def get(self, name):
#         return names[name]
#     # def post(self):
#     #     return {"data": "posted"}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    def post(self, video_id):
        return

# api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(Video, "/video/<int:video_id>")


if __name__ == '__main__':
    app.run(debug=True)
