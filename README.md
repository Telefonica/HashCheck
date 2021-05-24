# Password_HashCheck 

This project aims to assist in the search for leaked passwords while maintaining a high level of privacy using the k-anonymity method.

To achieve this, the APIs of different services are used, sending only a part of the Hash of the password we want to check, for example, the first 5 characters.

## Prerequisites

The project needs some libraries in order to work, to install it use the next command:

```python
pip install -r requirements
```

Remember that Python 3 is required.

## Usage

```python
passme.py [FUNC] [ELEMENT] -engine [ENGINE] -api_key [API_KEY]
```

        FUNC:       The kind of element tha you want to check, it can be -h/--hash or -p/--password
                    or -f/--file or -l/--list or --help.

        ELEMENT:    The "Hash", "Password" or the name of the file that contains a list of 
                    hashes or password separeted by a new line.

        ENGINE:     The leaks engine that you want to be used, by default it uses HIBP (Have I been PWN).

        API_KEY:    The API_KEY necessary for some functions of some engines.

## Functions

### PASSME_HASH

The main project function receives the hashed password, the engine to be used and the API key.

Depending on the engine that is received, both the API key and the hashed password will be sent to one function or another.

If you want to add your own engine or an engine that is not already implemented, simply add one more option here.

```python
passme_hash(hashed_password, engine="HIBP", api_key="0")
```

### PASSME_PASSWORD

This function hashes the password it receives using SHA-1 and sends the hash to the passme_hash() function.

```python
passme_password(password, engine="HIBP", api_key="0")
```

### PASSME_FILE

This function reads one by one the lines of the received file to check each password, giving information about the received password and whether it has been filtered or not.

```python
passme_file(filename, engine="HIBP", api_key="0")
```

### PASSME_LIST

This function reads one by one the lines of the received file to check each hash, giving information about the received hash and whether it has been filtered or not.

```python
passme_list(filename, engine="HIBP", api_key="0")
```

### PASSME_LIST

The function that deals with the HIBP (Have i been pwned) API, sends the first five characters of the hash, then compares it with the full hash to see if the password/hash has been leaked.

```python
engine_HIBP(hashed_password, engine, api_key)
```

# Test

This project has a series of tests to check the correct operation of all its functions, for this purpose the "pytest" library has been used. To run the tests, install pytest with the following command:

```python
pip install pytest
```

Once installed, simply run the "pytest" command to have the tests run automatically, any errors encountered will be returned by the terminal.

The results of the test in the lab are the following:

| Python Version |    Function Hash   |    Function List   |  Function Password |     RANDOM Hash    |   RANDOM Password  |                                  Comment                                  |
|:--------------:|:------------------:|:------------------:|:------------------:|:------------------:|:------------------:|:-------------------------------------------------------------------------:|
|       3.9      | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |                                                                           |
|       3.8      | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |                                                                           |
|       3.7      | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |                                                                           |
|       3.6      | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |                                                                           |
|       3.5      | :white_check_mark: | :white_check_mark: | :white_check_mark: |         :x:        |         :x:        | Random.choice is not available in Python 3.5 // Deprecated Python Version |
# License

This project is licensed under the GNU General Public License - see the LICENSE file for details

# Contact

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

This software doesn't have a QA Process. This software is a Proof of Concept.

If you have any problems, you can contact:

<ideaslocas@telefonica.com> - *Ideas Locas CDCO - Telefónica*


# Disclaimer

In many places it can be a crime to install software on a computer that does not belong to you, without the owner's consent. We do not approve the use of PoC for any illegal purpose.  To download or use our software in any way, you must acknowledge and approve the following:

1 - You declare that this PoC will be used exclusively in a legal manner. If you are in doubt as to the legality, consult a licensed attorney in the jurisdiction where you will be using this PoC.

2 - You acknowledge that the computer on which the software is to be installed is yours or you have the owner's consent to manage and install the software on it.