import mysql.connector
from difflib import get_close_matches
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()
word=input("Enter the word: ")
query = cursor.execute("SELECT Expression FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()
print(get_close_matches(word,results))

# if results:
#     for result in results:
#         print(result[0])
# else:
#     print("No word found!")

# def translate(word):
#     word= word.lower()
#     if word in data:
#         return data[word]
#     elif len(get_close_matches(word,data.keys()))>0:
#         close_word = get_close_matches(word, data.keys())[0]
#         prompt =input( "Did you mean '%s' instead? Press 'Y' for Yes (or) 'N' for No " % close_word).lower()
#         if prompt=="y":
#             return data[close_word]
#         elif prompt=="n":
#             return "Make Sure the Entered Word is Correct"
#         else:
#             return "We didn't understand your Entry"

#     else:
#         return "Make Sure the Entered Word is Correct"
# if __name__ == '__main__':
#     while True:
#         w = input("Enter a Word (or) Press 'E' to close the Program:")
#         if w.lower() =='e':
#             break
#         output = translate(w)
#         if type(output) == list:
#             count =1
#             for i in output:
#                 print(count,'.',i)
#                 count+=1
#         else:
#             print(output)
