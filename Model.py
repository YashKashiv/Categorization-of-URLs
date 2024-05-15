import requests
import json
import csv

def check_url_category(api_key, url):
    url = "https://api.webscategorizer.com/lookup/v1/obfuscate?key={}&url={}".format(api_key, url)
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        if data['categories']:
            return data['categories'][0]['label']
        else:
            return "No category found"
    else:
        return "Error occurred while fetching data"

def read_urls_from_csv(csv_file):
    urls = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            urls.extend(row)
    return urls

def write_urls_with_categories_to_csv(urls, categories, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Category'])
        for url, category in zip(urls, categories):
            writer.writerow([url, category])

def main():
    api_key = 'uo0xzGoVpGywbI3lrDAd'
    
    csv_file = 'urls.csv'
    urls = read_urls_from_csv(csv_file)
    
    categories = []
    for url in urls:
        category = check_url_category(api_key, url)
        categories.append(category)

    output_file = 'urls_with_categories.csv'
    write_urls_with_categories_to_csv(urls, categories, output_file)
    print("URLs and their categories saved to:", output_file)

if __name__ == "__main__":
    main()
