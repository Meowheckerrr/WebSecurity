from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/search" method="get">
            <label for="query">Search:</label>
            <input type="text" id="query" name="query">
            <input type="submit" value="Search">
        </form>
    '''

@app.route('/search')
def search():
    query = request.args.get('query', '')
    #XSS Here ! 
    return render_template_string(f'''
        <h1>Search Results for: {query}</h1>
        <p>No results found for your query.</p>
        <a href="/">Go back</a>
    ''')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)