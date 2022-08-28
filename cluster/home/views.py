from django.shortcuts import render
from django.http import HttpResponse
from kubernetes import client, config

# Create your views here.
def display_nodes(request):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    nodes = v1.list_node().items
    return render(request, 'nodes.html', {'data': nodes})


def display_pods(request):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    all_pods = v1.list_pod_for_all_namespaces()
    return render(request, 'pods.html', {'data': all_pods.items})