#!/usr/bin/env python3
""" This script contains the `top_students` function """


def top_students(mongo_collection):
    """  returns all students sorted by average score """
    docs = []
    for doc in mongo_collection.find():
        scores = 0
        for topic in doc['topics']:
            scores += topic['score']
        doc['averageScore'] = scores / len(doc['topics'])
        docs.append(doc)

    for idx, item in enumerate(docs):
        if idx < len(docs) - 1:
            if item.get('averageScore') < docs[idx + 1].get('averageScore'):
                docs[idx], docs[idx + 1] = docs[idx + 1], docs[idx]
                i = idx
                while i > 0:
                    if docs[i].get('averageScore') > docs[i - 1].get(
                            'averageScore'):
                        docs[i], docs[i - 1] = docs[i - 1], docs[i]
                        i -= 1
                    else:
                        break

    return docs
