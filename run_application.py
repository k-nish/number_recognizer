import os
import tornado.ioloop
import tornado.httpserver
import tornado.escape
from tornado.options import define, options
from application.server import Application

# Define command line arguments
define("port", default=3000, help="run on the given port", type=int)

# def split_dataset(dataset, test_size=0.3):
#     from sklearn import cross_validation
#     from collections import namedtuple

#     DataSet = namedtuple("DataSet", ["data", "target"])
#     train_d, test_d, train_t, test_t = cross_validation.train_test_split(dataset.data, dataset.target, test_size=test_size, random_state=0)

#     left = DataSet(train_d, train_t)
#     right = DataSet(test_d, test_t)

#     return left, right

# # use 30% of data to test the model
# training_set, test_set = split_dataset(digits, 0.3)
# print("dataset is splited to train/test = {0} -> {1}, {2}".format(
#         len(digits.data), len(training_set.data), len(test_set.data))
#      )

def main():
    # tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    port = int(os.environ.get("PORT", options.port))
    print("server is running on port {0}".format(port))
    http_server.listen(port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
