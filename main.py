import tweepy
import shutil
import json
import wget
import tqdm
import os


def get_ids():
	with open("ids/ids_devset.json", "r") as f:
		dev_ids = json.load(f)

	with open("ids/ids_testset_final.json", "r") as f:
		test_ids = json.load(f)

	return dev_ids, test_ids


def download_set(api, ids, folder):
	sucess, error = 0, 0
	for element in tqdm.tqdm(ids):
		try:
			status = api.get_status(element)
			media = status.entities.get('media', [])
			if(len(media) > 0):
				content = media[0]['media_url']
				extension = content.split(".")[-1]
				file_name = "./{}/{}.{}".format(folder, element, extension)
				wget.download(content, out=file_name, bar=None) 
				sucess += 1
		except tweepy.error.TweepError:
			error += 1

	return sucess, error


def create_api():
	with open("configs.json", "r") as f:
		content = json.load(f)

	auth = tweepy.OAuthHandler(content['consumer_key'], content['consumer_secret'])
	auth.set_access_token(content['access_token'], content['access_secret'])
	return tweepy.API(auth)


def create_folder(name):
	if os.path.exists(name):
		shutil.rmtree(name)
	os.mkdir(name)
	return name


def main():
	api = create_api()
	dev_ids, test_ids = get_ids()

	print("Downloading dev images  ...")
	sucess_dev, error_dev = download_set(api, dev_ids, create_folder("devset_images"))
	print("Donwloading test images ...")
	sucess_tst, error_tst = download_set(api, test_ids, create_folder("testset_images"))
	print("Done.")

	print("Development set : {}/{}".format(sucess_dev, sucess_dev + error_dev))
	print("Test set        : {}/{}".format(sucess_tst, sucess_tst + error_tst))



if __name__ == '__main__':
	main()
