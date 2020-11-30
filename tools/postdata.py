from configuration.config import collection

def insert_review(title, review):

    '''
    This function has two functionalities. The first one is, that it enables the user to update new reviews of a
    certain title. So if someone wants to write his opinion, it is enough to write the title and the review he wants
    to add.

    The second functionality is, that if a title does not exits in the database, it creates a new object with the same
    structure as the rest. This is possible thanks to the upsert = True.
    '''


    collection.update_one(
        {"title": f'{title}'},
        {"$push": {"reviews": f'{review}'}}, upsert=True
    )

    return 'Successful addition addition'



