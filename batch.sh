urls=(
  # https://jable.tv/videos/xxx-nnn/
)
find . -type d -empty -delete
for url in ${urls[@]}; do
  echo "./main.py --url ${url}"
  ./main.py --url ${url}
done
