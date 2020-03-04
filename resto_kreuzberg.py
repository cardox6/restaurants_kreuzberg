import sqlite3

#db queries
def db_query():
    db_connection = sqlite3.connect('./restaurants.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute('''SELECT name
    FROM restaurants
    WHERE NEIGHBORHOOD_ID="1";''')
    list_kreuzberg = db_cursor.fetchall()
    db_connection.close()
    return(list_kreuzberg)

# HTML Elements
HTML_start ="""
    <!DOCTYPE html>
    <html>
    <head>
    <meta>
    <title>Restaurant Finder</title>
    <link rel="stylesheet" href="/style.css">
    <body>
    <h1> Neighbourhood: Kreuzberg</h1>
    """

HTML_end ="""</body>\n</html>
        """
def another_list(list_kreuzberg):
    clean_list = """"""
    for restaurant in list_kreuzberg:
        clean_list +=  (f'<li class="headline, item">{restaurant[0]}</li>\n')
    return("<div>\n" + clean_list + "</div>")

def main_html(list_kreuzberg):
    
     return str(HTML_start) + str(another_list(list_kreuzberg)) + str(HTML_end)