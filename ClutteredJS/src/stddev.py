import os
import pandas as pd
import statistics
import csv

OUTPUT_FOLDERS = {"cluttered":"output.nw", "de-cluttered":"output.jsc"}

def find_paths(folder):
    return [x[0] for x in os.walk('output.nw') if 'batterystats' in x[0]]

def calc_stat(path):
    file_list = [ x for x in os.listdir(path) if 'Joule_' in x]

    def _read_file(file_path):
        pd_data = pd.read_csv(path + "/" + file_path)
        return pd_data.loc[0].values[0]

    readings = [_read_file(x) for x in file_list]

    return statistics.mean(readings), statistics.stdev(readings)

if __name__ == '__main__':
    with open('expirement_stats.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Subject', 'Treatment', 'Average', 'StdDev'])
        for treatment, folder in OUTPUT_FOLDERS.items():

            paths = find_paths(folder)
            for webpagepath in paths:
                avg, std = calc_stat(webpagepath)

                subject = webpagepath.split('/')[4]
                filewriter.writerow([subject, treatment, avg, std])

        