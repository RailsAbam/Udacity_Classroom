

letters = ["Ruby is a  future programmer, She will need to be taught now"]
second_letters = ["Her faourite Langauge is Ruby and Rails"]

string_ = "<ul>\n","<h1>\n"
for tem in letters and second_letters:
    string_ += "<p> {} </p>\n", "<h2> {} </h2>\n".format(tem)
    string_ += "</ul>","</h1>"

print(string_)