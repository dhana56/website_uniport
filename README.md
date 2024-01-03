# Website: UniProt-id Retrieval 
> The website retrieves the UniProt ID of the protein chain. It takes the list of PDB id as input and returns the Uniport by chain name. This simple website is built from the Flask framework.

> [!NOTE]
>Before Running the program files, <br>
 1. Set up a virtual environment. For setting up the virtual environment, visit [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
   
 2. After setting up the virtual environment run [requirement.txt](requirement.txt) in the terminal window where the programic Folder is located.
   <pre>      pip install requirement.txt</pre>
 3. Before running [app.py](app.py) file. Please set up the flask variable. More detailed info on how to set up is provided [here](https://flask.palletsprojects.com/en/1.1.x/config/)
 4. After setting up the above instructions. Run the [app.py](app.py) 
   <pre>                python app.py</pre>

> Flask website directory tree:
> <pre> 
>           FLASK_DEV
>           ___|
>           |---static
>           |       |-- style.css
>           |---templates
>           |        |-- base.html
>           |        |-- index.html
>           |        |-- user.html
>           |--app.py
>           |fun.py </pre>
>
## Website
The demo view of the Uniport-id retrieval  website is shown below:<br>
<br>
<img src="entry.png" alt="Website home page" align="center" width="500" height="300">

<img src="unport.png" alt="result.png" align="center" width="500" height="300">
<br>
