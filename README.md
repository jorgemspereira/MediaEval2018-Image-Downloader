# MediaEval2018-Image-Downloader
Small python script that allows downloading the images from the dataset of the Multimedia Satellite Task of MediaEval 2018. 

To use this script you will need a set of credentials from a Twitter's Application, this means that you have to create a Twitter's dev account.
After your account is approved, create a json file named *configs.json* with the following keys:

```json
{
  "consumer_key": "",
  "consumer_secret": "",
  "access_token": "",
  "access_secret": ""
}
```

Next, you only need to run the script to download the images!

```bash
python3 main.py
```
