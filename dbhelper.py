import mysql.connector


class DBHelper:
    def __init__(self):

        # in database two tables have been created
        # 1.users-user_id,name,email,password
        # 2.expenses-expenseType,amountSpent,date
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="expensetracker")


            self.mycursor = self.conn.cursor()
            print("Database connection successful")

        except:
            print("Not connected")

    # checking the credentials for login
    def checkLogin(self,email,password):

        query = "SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'".format(email, password)
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()


        return data
    # registering new users in the database
    def performRegistration(self, name, email, password):

        query = "INSERT INTO users (user_id,name,email,password)VALUES(NULL,'{}','{}','{}')".format(
            name, email, password);

        try:

            self.mycursor.execute(query)



            self.conn.commit()

            return 1

        except:
            return 0

   # adding new expenses in the database
    def performAddExpense(self,user_id,expenseType,amountSpent,date):
        query="INSERT INTO `expenses`(`user_id`, `expense_type`, `amount`, `date`)VALUES('{}', '{}', '{}', '{}')".format(user_id,expenseType,amountSpent,date)
        #print(query)

        try:

            if amountSpent==0 or expenseType==''or date=='':
                return 0

            self.mycursor.execute(query)


            self.conn.commit()

            return 1


        except:

                return 0






    # calculating the total expenditure by the user
    def performtotalSpending(self,user_id):
        query = "SELECT sum(amount) as totalSpending from expenses where user_id='{}'".format(user_id)
        # print(query)
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        # print(result)
        return result

    # showing the details of all the expenses entered by the user
    def performViewExpenses(self,user_id):

        query="SELECT * FROM `expenses` WHERE user_id='{}'".format(user_id)
        try:
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()
            # print(data)
            return data
        except:
            return 0
    # editing the amount on the basis of expense type, date entered by the user
    def editExpenses(self,expenseType,amountSpent,date,user_id):
        query = "UPDATE expenses SET amount='{}'WHERE user_id={} and expense_type='{}' and date='{}'".format(
             amountSpent,user_id,expenseType,date)
        # print(query)

        try:
            if amountSpent == 0 or expenseType == '' or date == '':
                return 0

            else:

                self.mycursor.execute(query)
                self.conn.commit()
                check = self.checkexpenses(user_id, expenseType, amountSpent,date)
                if check==0:
                    return 1



        except:
            return 0



    def deleteExpenses(self,user_id,expenseType,amountSpent,date):
        query = "DELETE FROM expenses WHERE user_id='{}'and expense_type='{}'and amount='{}'and date='{}'".format(
            user_id,expenseType, amountSpent, date);
        # print(query)

        try:
            response = self.checkexpenses(user_id,expenseType,amountSpent,date)
            if response == 0:
                self.mycursor.execute(query)
                self.conn.commit()
                return 1


        except:
            return 0

    # to check if the data entered by the user is present in the database
    def checkexpenses(self,user_id,expenseType,amountSpent,date):

        query="SELECT * FROM `expenses` WHERE `user_id` ='{}' AND `expense_type` LIKE '{}' AND `amount` = {} AND `date` LIKE '{}'".format(user_id,expenseType,amountSpent,date)

        # print(query)
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        # print(data)
        # print(len(data))

        # return data

        if len(data) > 0:
            return 0

        else:
            return 1













