## Dependencies

We are using [Appium-Python-Client](https://github.com/appium/python-client) as the wrapper for Appium in Python.

You can install it with `pip`
```
$ pip install Appium-Python-Client
```

## Running your tests

- Do remember to switch the BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY with your own browserstack credentials.
- Upload your Native App (.apk file) to BrowserStack servers using upload API and update the app capability:

  ```
  curl -u "username:accesskey" -X POST "https://api.browserstack.com/app-automate/upload" -F "file=@/path/to/app/file/Application-debug.apk"
  ```

- If you do not have an .apk file and looking to simply try App Automate, you can download our [sample app](https://www.browserstack.com/app-automate/sample-apps/android/WikipediaSample.apk) and upload to the BrowserStack servers using the above API.
- Update the desired capability "app" with the App URL returned from the above API call

For running LocalSample tests, you can download the latest local binary from [here](https://www.browserstack.com/local-testing) and run it as specified in the docs. Pass the `browserstack.local` capability as `True` and run the appium wrapper as usual.
