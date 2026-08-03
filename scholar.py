n = int(input())
movies = []
for i in range(n):
    movies.append(tuple(map(int, input().split())))

movies.sort(key=lambda m: m[1])

moviecount = 0
endtime = 0

for s, e in movies:
    if e >= endtime:
        endtime = e
        moviecount += 1