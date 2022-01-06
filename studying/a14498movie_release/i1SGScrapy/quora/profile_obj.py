class Profile:
    def __init__(self, name, url=None, bio=None, followedby=None):
        self.name = name
        self.url = url
        self.bio = bio
        self.followedby = followedby

    def merge(self, other):
        if not self.url:
            self.url = other.url
        if not self.bio:
            self.bio = other.bio

    def __repr__(self):
        return "Profile:{}, {}, {}, {}".format(self.name, self.url, self.bio, self.followedby)

    def dictstyle(self):
        return {'name': self.name, 'url': self.url,
                'bio': self.bio, 'followedby': self.followedby}


def merge_lists(list_1, list_2):
    output = {p.name: p for p in list_1}
    for p in list_2:
        try:
            output[p.name].merge(p)
        except KeyError:
            output[p.name] = p
    return list(output.values())


class Question:
    def __init__(self, name, followedby=None):
        self.name = name
        self.followedby = followedby

    def dictstyle(self):
        return {'name': self.name, 'followedby': self.followedby}


class ProfileSummary:
    def __init__(self, lastfollowingnum=None, lastname=None,
                 lastquestionnum=None, lastquestion=None):
        self.lastfollowingnum = lastfollowingnum
        self.lastname = lastname
        self.lastfollowingnum = lastquestionnum
        self.lastquestion = lastquestion
