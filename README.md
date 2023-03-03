<h1>End to End University Enquiry Chatbot (using NLP)</h1>
<p>This project is an end-to-end university enquiry chatbot that uses natural language processing (NLP) to understand and respond to user queries related to the university. The chatbot is trained on a set of intents that cover various topics such as admissions, courses, fees, campus facilities, etc. The user can interact with the chatbot via a CLI or GUI interface and get quick and accurate responses to their queries.</p>

<h2>Live Demo</h2>

<p>You can check out a live demo of the chatbot <a href="https://nkevin90.github.io/Kabarak-University-Chatbot/">here</a>.</p>

<h2>Installation and Setup</h2>

<p>This project requires the following packages and dependencies:</p>

<ul>
    <li>Python 3.6 or higher</li>
    <li>TensorFlow 2.x or higher</li>
    <li>NumPy</li>
    <li>NLTK</li>
    <li>Flask</li>
    <li>Flask-SocketIO</li>
    <li>JSON</li>
</ul>

<p>To install these packages, you can use pip:</p>

<pre><code>pip install tensorflow numpy nltk flask flask-socketio json</code></pre>

<h2>Training the Model</h2>

<p>To train the model, run the <code>train.py</code> script:</p>

<pre><code>python train.py</code></pre>

<p>This will train the model on the intents defined in the <code>intents.json</code> file.</p>

<p>If you want to modify the intents, you can edit the <code>intents.json</code> file and then retrain the model.</p>

<h2>Running the CLI Interface</h2>

<p>To run the chatbot on the CLI interface, run the <code>chat.py</code> script:</p>

<pre><code>python chat.py</code></pre>

<p>This will start the chatbot on the command line.</p>

<h2>Running the GUI Interface</h2>

<p>To run the chatbot on the GUI interface, run the <code>app.py</code> script:</p>

<pre><code>python app.py</code></pre>

<p>This will start the chatbot on the GUI interface and generate a link. Open the link in your browser to interact with the chatbot.</p>

<h2>Screenshots</h2>

<p>Here are some screenshots of the chatbot in action:</p>

<img src="Screenshots/Screenshot (48).png" alt="Screenshot 1">

<img src="Screenshots/Screenshot (50).png" alt="Screenshot 2">

<img src="Screenshots/Screenshot (56).png" alt="Screenshot 3">

<h2>Improvements</h2>

<p>This project is open to improvements. Some areas to improve on include:</p>

<ul>
    <li>Adding more intents and responses to the <code>intents.json</code> file</li>
    <li>Adding more features to the GUI interface, such as voice recognition and text-to-speech capabilities</li>
    <li>Improving the accuracy of the model by using more advanced techniques such as BERT or transformers</li>

