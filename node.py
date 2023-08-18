'''
node.py
Part of the graph traversal algorithm using connected nodes prototype.
'''
import math

class Node:
    '''
    Identifies the node class and all node operations.
    'node_pos' is the x,y coordinates in a list.
    'connected_nodes' are in list format.
    '''

    def __init__(self, node_id, node_type=None, node_pos=None, connected_nodes=None):
        # Node ID should be provided and be a unique value.
        self.node_id = node_id
        self.node_type = node_type

        # Set node_pos[x,y] to 0,0 if not defined
        self.node_pos = node_pos if node_pos is not None else [0,0]
        self.connected_nodes = connected_nodes

        # Sets node initial state to 'init'
        self.state = 'init'

        # When a node changes state, it knows which node changed it.
        self.previous_node = None

        # Node's score is set to an initial value
        self.score = 0


    def open_node(self, opening_node):
        ''' Set a state to be open, ready for evaluating '''
        self.state = 'open'
        # Sets previous_node to the node that opened it
        self.previous_node = opening_node


    def close_node(self):
        ''' Set a state to closed, after evaluation has completed '''
        self.state = 'closed'
        self.score = 0


    def score_node(self, endnode, previous_node):
        '''
        Score the node based on the following formula:
        dist_to_end_node + dist_to_previous_node + previous_node_score
        This heuristic will probably change. 
        '''
        dt_endnode = math.dist(endnode.node_pos, self.node_pos)
        dt_previous = math.dist(previous_node.node_pos, self.node_pos)

        self.score = dt_endnode + dt_previous + previous_node.score
        return self.score
