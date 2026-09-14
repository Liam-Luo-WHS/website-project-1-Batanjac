vote_count = 0
movie_votes = []

people = int(input("How many people are voting? "))

while vote_count != people:
    vote = input(f"Person {vote_count+1}, enter a movie: ")
    movie_votes.append(vote)
    vote_count += 1
print(movie_votes)

#Figure out how to make the same input count as a vote
if vote_count == people:
    print("")