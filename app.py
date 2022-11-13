from flask import Flask, request, render_template
from Detection_of_Groups_with_Biased_Representation_in_Ranking.Coding.Algorithms.IterTD_GlobalBounds\
    import GraphTraverse as GraphTraverseNonProportional
from Detection_of_Groups_with_Biased_Representation_in_Ranking.Coding.Algorithms.IterTD_PropBounds\
    import GraphTraverse as GraphTraverseProportional



app = Flask(__name__)


@app.route('/GraphTraverseNonProportional', methods=['POST'])
def index():
    task_content = request.form['content']
    ranked_data = task_content['task_content']
    attributes = task_content['attributes']
    Thc = task_content['Thc']
    Lowerbounds = task_content['Lowerbounds']
    k_min = task_content['k_min']
    k_max = task_content['k_max']
    pattern_treated_unfairly_lowerbound, num_patterns_visited, time = GraphTraverseNonProportional(ranked_data, attributes, Thc, Lowerbounds, k_min, k_max, 60*10)
    return pattern_treated_unfairly_lowerbound
    return "Hello, world!"

@app.route('/GraphTraverseProportional', methods=['POST'])
def index():
    task_content = request.form['content']
    ranked_data = task_content['task_content']
    attributes = task_content['attributes']
    alpha = task_content['alpha']
    k_min = task_content['k_min']
    k_max = task_content['k_max']
    pattern_treated_unfairly_lowerbound, num_patterns_visited, time = GraphTraverseProportional(ranked_data, attributes, Thc, Lowerbounds, k_min, k_max, 60*10)
    return pattern_treated_unfairly_lowerbound
    return "Hello, world!"

@app.route('/emi', methods=['GET'])
def index():
    error = None
    return render_template('../web/home.html')

if __name__ == "__main__":
    app.run(debug=True)