post = input("Enter your post:")

# if("Varun" in post):
# this will not work because varun can be in any form for eg VaRun, VARUn, etc

if("varun" in post.lower()):
    print("Post is talking about Varun")

else:
    print("Post is not talking about Varun")
