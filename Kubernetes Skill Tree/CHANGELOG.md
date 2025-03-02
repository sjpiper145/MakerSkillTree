# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## Peer Review 1 [Unreleased]

### Added

* More steps to create familiarity with commonly used parts of the sprawling `kubectl` command.
* Steps to bringing your own application to Kubernetes:
    * "Use an image from a private container repository"
    * "Create a container from your app"
* Introduction to additional tools:
    * "Try an alternative to kubectl like K9s"
    * "Install the Kubernetes Dashboard"
* Milestones for beginner/intermediate/advanced use cases:
    * Beginner: "Deploy apps for your personal use"
    * Intermediate: "Run apps for a club on a cluster"
    * Advanced: "Host apps on the Internet from your cluster"
* Places to get more information:
    * "Explore kubectl's "Troubleshooting" section"
    * "Explore the Kubernetes Reference Guide"
    * "Explore the Kubernetes Tutorials"
* More gradual exposure to different concepts:
    * "Set up health check probes on your workloads" for the different kinds of health checks
    * "Set up two workloads that communicate" for in-cluster DNS
    * "Deploy a stateless app" the first major step after a Hello, World Pod is deploying 
      something that doesn't need to store data.
    * "Expose a Deployment using a Service" step to show that Deployments and Pods work similarly.
    * "Create a multi-container Pod" for sidecars
    * "Use headless Services for service discovery" for service discovery
    * "Deploy a non-HTTP workload e.g. FTP server" for TCP networking, which is more primitive
    * "Optimize your workload container sizes" for cost savings and performance
    * "Set up ServiceAccounts for your workloads" for security and cluster sharing
    * "Share your cluster with a second person" for practical RBAC
    * "Configure a Deployment for high availability updates" for proper use of Deployments
* Different options to get Kubernetes clusters:
    * "Deploy a cluster in the cloud" this is what most people do.
    * "Set up a cluster from scratch on Raspberry Pis" a common approach for hobbyists with lots of info and
      varying degrees of difficulty depending on how deep into it you want to go.
* Basic operations needs:
    * Learn how to backup and restore your cluster
    * Make your cluster reproducible with Terraform

### Changed

* "Create a basic Pod" to "Deploy a 'Hello, World!'' Pod" because it's not obvious what "basic" means.
* "Secure sensitive data with Secrets" to "Use a Secret to distribute credentials" because Secrets don't
  provide much security.
* Merged "Set resource requests for Pods" and "Set resource limits for Pods" to 
  "Set resource requests and limits for workloads" because it's the same topic.
* "Perform rolling updates and rollbacks" to "Roll back a change to a Deployment" rolling updates are the default, 
  but being able to undo a mistake is very important.
* Merged "Control Pod scheduling tolerations" and "Configure Pod affinity and anti-affinity" into 
  "Control scheduling with tolerations and affinity" because they're similar topics.
* Replaced "Set up Persistent Volumes and Claims" and "Create StatefulSets for stateful applications" with "
  Deploy Wordpress and MySQL with Persistent Volumes" to focus on an outcome. This wil point you at the Kubernetes.io 
  tutorial for stateful workloads.
* Consolidated topics related to operators and CRDs into: "Develop your own operator and CRDs". This is a niche skill,
  but it's good to know it's possible.
* Consolidated multiple service mesh/advanced networking related solutions to "Deploy a service mesh to your cluster"
* Consolidated multiple monitoring items to: "Set up cluster-wide logging and monitoring" and 
  "Set up alerting for unhealthy workloads". Logging/monitoring are usually the same tool and useful by themselves.
* Many small wording changes to improve cohesion.

### Removed

* "Use Kubectl to manage resources" because it has high overlap with the other skills.
* Duplicate "Expose a Pod using a Service"
* "Apply network policies to control traffic between Pods" because only some configurations support this out of the box,
  it silently fails otherwise which would be frustrating for a beginner.
* Skills that focus on specific parts of deploying your own cluster, these align better with a platform engineer role 
  than a hobbyist. Some of these are now covered by deploying a cluster on a Raspberry Pi:
    * "Set up a container runtime e.g. Containerd, CRI-0" 
    * "Set up ingress for external access e.g. NGINX, Traefik"
    * "Set up a multi-node cluster with kubeadm"
    * "Set up a cluster using Kubeadm"
    * "Use Cluster API"
    * "Use Kubernetes on Bare Metal"
    * "Use persistent volume provisioners"
    * "Install and configure a networking solution e.g. Calico, Flannel"
* Removed multiple items related to storage, these should be covered enough to get by with the stateful application tile:
    * "Use external storage solutions with Kubernetes"
    * "Configure storage class"
    * "Implement storage solutions with CSI drivers"
* Removed multiple skills that start to matter when you have lots of people or large clusters:
    * "Optimize costs within Kubernetes" partially covered by optimizing workloads
    * "Use OPA for policies"
    * "Perform cluster performance tuning" 
    * "Implement GitOps practices" partially covered elsewhere
    * "Create a blue-green deployment" not best practice in Kubernetes
    * "Create a canary deployment" already covered with Deployments

### Fixed

* Various capitalization issues.
    * `Kind` to `kind` to match their website
    * `MiniKube` to `minikube` to match their website
    * Capitalized Kubernetes types except namespace to be consistent with kubernetes.io