# Covert Networks: How Hard is It to Hide?

## Abstract

Covert networks -> social networks that often consist of harmful users.

Social Network Analysis (SNA) has played an important role in reducing criminal activities (e.g., counter terrorism) via detecting the influential users in such networks.

*What is NP-complete?*

## Introduction

Security personnel regularly use various SNA tools to understand criminal behavior, catch their leaders, and effectively dismantle such networks [27, 30, 40].

There are many different ways we can create the vertices based on their relative influence or importance in the network. Higher scores may correspond to important vertices and important vertices re expected to be more central. We can look at the different centrality methods. I think degree centrality will be our thing or core centrality which they say is better. Core centrality also considers its neighbors so we should probably use this one.

Indeed, understanding covert networks remains a challenging task mainly due to incompleteness and dynamic evolution of the data as well as the strategic nature of the users.

## Contribution

We observe that our algorithm almost always produces near optimal results in practice. In the experimental results, we also show the extent in which a leader can hide in the captain network with respect to core centrality.

## Captain Networks

Captains spread the influence of the leader.

## Network Centrality

Intuitively, centrality measures try to capture the importance of a vertex in a network.

## Captain Networks and Core Centrality

- A captain network with small number of leaders and a large number of captains in each group produces the maximum amount of disguise.

- A small number of captains in each group yields lower disguise for core centrality which is not true for other centralities such as degree, closeness, and betweenness.

## Conclusion and Future Work

An important future direction is to explore the average case computational complexity of the **Hiding Leader** problem for popular network centrality measures.\

Talks about randomly generated data.

Another immediate future work is to resolve the computational complexity of the **Hiding Leader** problem for the core centrality measure when the core centrality of every leader is at most 2.
