from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)
CORS(app)
api = Api(app)

#######################################################################################################################
# Starting from the square informed, I walk 5 columns positively and then 5 columns of negative form,
# for each column I verify some varieties of possibilities in the lines as per rule below:
#
# In column 0 the line advances by 2 in 2 starting from 0 and ending in 5.
#
# In column 1 the line advances 2 by 2 starting at 1 and ending at 4.
#
# In column 2 the line advances by 4 by 4 starting at 0 and ending at 5.
#
# In column 3 the line advances 2 by 2 starting from 0 and ending 4.
#
# In column 4 the line advances by 2 by 2 starting at 0 and ending at 3.
#
# Advance on these lines in a positive and negative way.
#
# Zero (initial column) is equal to the column reported by the web application and
# the Zero line (initial line) is equal to the line reported by the web application.
#######################################################################################################################
class Chess(Resource):

    def get(self, squareId):

        # Constants list to mount the matrix.
        colArr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        # Variables to execute the functions.
        position = [0 for i in range(2)]
        response = [[] for i in range(2)]


        # Mount the Matrix for the Chessboard.
        chessBoard = [[str(colArr[y]) + "" + str(8 - x)
                       for x in range(len(colArr))] for y in range(len(colArr))]


        # Checks if the Column and Row is larger or smaller than the final and
        # initial Column or Row of the Matrix.
        def verifyPosition(col, lin):
            if len(colArr) > col >= 0:
                if len(colArr) > lin >= 0:
                    return True

            return False


        # Receiving the front-end variable and taking its position on the Chessboard.
        def catchStartingPositions(val):

            for x in range(len(colArr)):
                for y in range(len(colArr)):
                    if chessBoard[x][y] == val:
                        position[0], position[1] = x, y

            return position


        # Search for squares to highlight in Turn One.
        def positionsTurnOne(initialCol, initialLine):

            result = []

            for x in range(initialCol + 1, initialCol + 3, 1):
                if x == initialCol + 1:
                    if verifyPosition(x, initialLine + 2):
                        result += [str(chessBoard[x][initialLine + 2])]

                    if verifyPosition(x, initialLine - 2):
                        result += [str(chessBoard[x][initialLine - 2])]

                if x == initialCol + 2:
                    if verifyPosition(x, initialLine + 1):
                        result += [str(chessBoard[x][initialLine + 1])]

                    if verifyPosition(x, initialLine - 1):
                        result += [str(chessBoard[x][initialLine - 1])]

            for x in range(initialCol - 1, initialCol - 3, -1):
                if x == initialCol - 1:
                    if verifyPosition(x, initialLine + 2):
                        result += [str(chessBoard[x][initialLine + 2])]

                    if verifyPosition(x, initialLine - 2):
                        result += [str(chessBoard[x][initialLine - 2])]

                if x == initialCol - 2:
                    if verifyPosition(x, initialLine + 1):
                        result += [str(chessBoard[x][initialLine + 1])]

                    if verifyPosition(x, initialLine - 1):
                        result += [str(chessBoard[x][initialLine - 1])]

            return result


        # Search for squares to highlight in Turn Two.
        def positionsTurnTwo(initialCol, initialLine):

            result = []

            for x in range(initialCol, initialCol + 5, 1):
                if x == initialCol:
                    for y in range(initialLine, initialLine + 5, 2):
                        if verifyPosition(x, y):
                            result += [str(chessBoard[x][y])]

                    for y in range(initialLine, initialLine - 6, -2):
                        if y != initialLine:
                            if verifyPosition(x, y):
                                result += [str(chessBoard[x][y])]

                if x == initialCol + 1:
                    for y in range(initialLine + 1, initialLine + 4, 2):
                        if verifyPosition(x, y):
                            result += [str(chessBoard[x][y])]

                    for y in range(initialLine - 1, initialLine - 5, -2):
                        if verifyPosition(x, y):
                            result += [str(chessBoard[x][y])]

                if x == initialCol + 2:
                    for y in range(initialLine, initialLine + 5, 4):
                        if verifyPosition(x, y):
                            result += [str(chessBoard[x][y])]

                    for y in range(initialLine, initialLine - 6, -4):
                        if y != initialLine:
                            if verifyPosition(x, y):
                                result += [str(chessBoard[x][y])]

                if x == initialCol + 3:
                    for y in range(initialLine + 1, initialLine + 4, 2):
                        if verifyPosition(x, y):
                            result += [str(chessBoard[x][y])]

                    for y in range(initialLine - 1, initialLine - 5, -2):
                        if verifyPosition(x, y):
                            result += [str(chessBoard[x][y])]

                if x == initialCol + 4:
                    for y in range(initialLine, initialLine + 3, 2):
                        if verifyPosition(x, y):
                            result += [str(chessBoard[x][y])]

                    for y in range(initialLine, initialLine - 4, -2):
                        if y != initialLine:
                            if verifyPosition(x, y):
                                result += [str(chessBoard[x][y])]

            for x in range(initialCol, initialCol - 6, -1):
                if x == initialCol - 1:
                    for y in range(initialLine + 1, initialLine + 4, 2):
                        if verifyPosition(x, y):
                            result += [str(chessBoard[x][y])]

                    for y in range(initialLine - 1, initialLine - 5, -2):
                        if verifyPosition(x, y):
                            result += [str(chessBoard[x][y])]

                if x == initialCol - 2:
                    for y in range(initialLine, initialLine + 5, 4):
                        if verifyPosition(x, y):
                            result += [str(chessBoard[x][y])]

                    for y in range(initialLine, initialLine - 6, -4):
                        if y != initialLine:
                            if verifyPosition(x, y):
                                result += [str(chessBoard[x][y])]

                if x == initialCol - 3:
                    for y in range(initialLine + 1, initialLine + 4, 2):
                        if verifyPosition(x, y):
                            result += [str(chessBoard[x][y])]

                    for y in range(initialLine - 1, initialLine - 5, -2):
                        if verifyPosition(x, y):
                            result += [str(chessBoard[x][y])]

                if x == initialCol - 4:
                    for y in range(initialLine, initialLine + 3, 2):
                        if verifyPosition(x, y):
                            result += [str(chessBoard[x][y])]

                    for y in range(initialLine, initialLine - 4, -2):
                        if y != initialLine:
                            if verifyPosition(x, y):
                                result += [str(chessBoard[x][y])]

            return result


        # Using the information received from the web application and finding positions in Chessboard matrix.
        position = catchStartingPositions(squareId)

        turnOne = positionsTurnOne(position[0], position[1])
        response[0] = turnOne

        turnTwo = positionsTurnTwo(position[0], position[1])
        response[1] = turnTwo

        return response

# Api route declaration
api.add_resource(Chess, "/chess/<string:squareId>")

app.run(debug=True)