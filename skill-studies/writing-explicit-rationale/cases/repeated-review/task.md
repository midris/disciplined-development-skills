Please address the open review on this change. The checkout contains the proposed changes; the attached patch shows the diff under review.

Round 1, reviewer: “Why duplicate the interactive limit checks? Move the guard into persist().”
Author reply: “The batch importer also uses persist() and receives already-approved records. Running the interactive admission check on that path would reject valid imports. We accepted two guards and agreed to reconsider factoring the interactive check out when a third interactive caller appears.”
Round 2, reviewer: “I still think the limit check belongs in persist(). Can we resolve this before merge?”

Release handover from Gateway: requests already in flight can carry the token issued before a quota downgrade. Immediately cutting their quota can reject previously admitted work. The agreed handover permits the higher quota on those tokens for up to 60 seconds after the change. New tokens use the new limit immediately.
