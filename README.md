# autocomplete_light_dynamic_example
Example of enabling and disabling autocompletion for a text input dynamically based on other form field values

Most commonly, autocompletion is defined for a particular form field in the Django form definition.  I had a requirement to set the value of a field to a sepcific value, or use autocompletion, or allow freeform input based on other factors.  In this example, the "other factors" are radio button settings.

The example would be better if the form was created with a Django form definition instead of my simple, raw HTML. Perhaps I will fix that in the future.

In order to test the example:

1. create a new virtualenv and activate it
2. ```pip install -r requirements.txt```
3. ```python manage.py runserver```
4. load the form from http://127.0.0.1:8000

When autocompletion is enabled, the initial characters you type should match one of the names in  ```example/autocomplete_light_registry.py```.

When you submit the form, you'll see the posted data on the Django console and the form will be ready to fill in and submit again for more experimentation.
