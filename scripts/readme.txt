# I used this to create the kubernetes cluster
gcloud container clusters create helloworld-gke    --num-nodes 1    --enable-basic-auth    --issue-client-certificate    --zone us-central1-c

# this to create the filestore
gcloud filestore instances create nfs-server     --project=ev-crawl     --zone=us-central1-c     --tier=STANDARD     --file-share=name="vol1",capacity=1TB     --network=name="default"
