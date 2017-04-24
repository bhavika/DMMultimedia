from gensim.models import LdaModel


# Visualize NYTimes topics
lda_20 = LdaModel.load('../models/lda_20.lda')
lda_30 = LdaModel.load('../models/lda_30.lda')
lda_40 = LdaModel.load('../models/lda_40.lda')


def display_topics(ldamodel, n):
    topics = ldamodel.show_topics(num_topics=n)

    for i in range(len(topics)):
        print topics[i]

print '30 topic model '
display_topics(lda_30, 30)

print '20 topic model'
display_topics(lda_20, 20)

print '40 topic model'
display_topics(lda_40, 40)


print "-------------------------------"


mnist_20 = LdaModel.load('../models/mnist_lda_20.lda')
mnist_50 = LdaModel.load('../models/mnist_lda_50.lda')
mnist_100 = LdaModel.load('../models/mnist_lda_100.lda')

print "20 MNIST topics"
display_topics(mnist_20, 20)

print "50 MNIST topics"
display_topics(mnist_50, 50)

print "100 MNIST topics"
display_topics(mnist_100, 100)

