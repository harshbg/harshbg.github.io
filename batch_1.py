from injector import inject_data

data = {
    'king-range': {
        'googleRating': 4.8,
        'googleReviews': "'1.2K'"
    },
    'alabama-hills': {
        'googleRating': 4.9,
        'googleReviews': "'1.8K'"
    },
    'carrizo-plain': {
        'googleRating': 4.6,
        'googleReviews': "'950'"
    },
    'berryessa-snow-mountain': {
        'googleRating': 4.5,
        'googleReviews': "'300'"
    },
    'san-gabriel-mountains-nm': {
        'googleRating': 4.7,
        'googleReviews': "'3.5K'"
    },
    'sand-to-snow-nm': {
        'googleRating': 4.6,
        'googleReviews': "'250'"
    },
    'santa-rosa-san-jacinto-nm': {
        'googleRating': 4.8,
        'googleReviews': "'450'"
    },
    'california-coastal-nm': {
        'googleRating': 4.9,
        'googleReviews': "'2.1K'"
    },
    'point-arena-stornetta': {
        'googleRating': 4.8,
        'googleReviews': "'320'"
    },
    'cotoni-coast-dairies': {
        'googleRating': 4.5,
        'googleReviews': "'120'"
    },
    'elkhorn-slough-reserve': {
        'googleRating': 4.8,
        'googleReviews': "'550'"
    }
}

if __name__ == '__main__':
    inject_data(data)
