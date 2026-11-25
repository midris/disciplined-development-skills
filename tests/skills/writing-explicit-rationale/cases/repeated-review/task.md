Please address the open review on this change. The checkout contains the proposed changes; the review system saved the submitted commit at review-input/change.patch.

Round 1, reviewer: “Why duplicate the interactive limit checks? Move the guard into persist().”
Author reply: “The batch importer also uses persist() and receives already-approved records. Running the interactive admission check on that path would reject valid imports. We accepted two guards and agreed to reconsider factoring the interactive check out when a third interactive caller appears.”
Round 2, reviewer: “I still think the limit check belongs in persist(). Can we resolve this before merge?”
