import os

def deleteMp4(folderPath):
    files = os.listdir(folderPath)
    originFile = folderPath.split(os.path.sep)[-1] + '.mp4'
    for file in files:
        if file != originFile:
            os.remove(os.path.join(folderPath, file))


def deleteM3u8(folderPath):
    files = os.listdir(folderPath)
    for file in files:
        if file.endswith('.m3u8'):
            os.remove(os.path.join(folderPath, file))

def deleteDownloadedURLFromBatch(url):
    with open("batch.sh", "r") as input:
        with open("temp.sh", "w") as output:
            for line in input:
                if str(url) not in line.strip("\n"):
                    output.write(line)
    # replace file with original name
    os.replace('temp.sh', 'batch.sh')
    os.chmod('batch.sh', 0o744)