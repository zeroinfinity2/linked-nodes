'''
The demo script for the graph traversal algorithm
'''
import csv
import node

def create_map(nodefile):
    '''
    Creates node objects based on file input.
    In essence, creates the map for pathfinding.
    Puts in dictionary
    '''
    nodelist = {}
    with open(nodefile, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            nodelist.update({
                row['node_id']:
                node.Node(row['node_id'],
                          node_pos=[int(row['node_x']),int(row['node_y'])],
                          connected_nodes=row['connected_nodes'].split())})
    return nodelist


def get_path(start_node, destination_node, map_nodes, open_nodes=None):
    '''
    The main algorithm.
    '''

    if open_nodes is None:  # If its our first time through
        open_nodes = []
        # Set start node to open state
        start_node.open_node(None)
        open_nodes.append(start_node)

    # Open Connecting nodes if the start and destination are not the same
    # Note that the starting node in this case WILL change on each execution
    # of this recursive function.
    if start_node.node_id != destination_node.node_id:
        for co_node in start_node.connected_nodes:

            if start_node.node_id != destination_node.node_id:
                if map_nodes[co_node].state == 'init':
                    # Open connecting node
                    map_nodes[co_node].open_node(start_node)
                    print(f'Node {map_nodes[co_node].node_id}: {map_nodes[co_node].state}')
                    print(f'Opened by: {map_nodes[co_node].previous_node.node_id}')

                    # Score Connecting nodes
                    map_nodes[co_node].score_node(destination_node, start_node)
                    print(f'{map_nodes[co_node].node_id} Score: {map_nodes[co_node].score}')

                    # Add open nodes to the open node list
                    open_nodes.append(map_nodes[co_node])

        # Close the originating node and remove from list
        start_node.close_node()
        print(f'Start node {start_node.node_id} closed.')
        open_nodes.remove(start_node)

        # Find the lowest score in the open nodes
        open_nodes.sort(key=lambda node: node.score)
        input(f'Lowest node: {open_nodes[0].node_id} = {open_nodes[0].score}')

        # Call the function again, setting the start as the lowest node.
        return get_path(open_nodes[0], destination_node, map_nodes, open_nodes)

    else:
        print('A path has been found!')
        # Begin pathing phase
        # Each node knows which node has opened it.
        path = []
        eval_node = destination_node
        while eval_node is not None:
            path.append(eval_node.node_id)
            eval_node = eval_node.previous_node
        path.reverse()
        return path


def main():
    '''
    Main function
    '''

    node_file = 'nodelist.csv'
    map_nodes = create_map(node_file)

    location = input('Enter your current location node (n1-n23):')
    print(f'Starting node: {map_nodes[location].node_id}')
    print(f'Starting Coordinates: {map_nodes[location].node_pos}')
    print(f'Connected Nodes: {map_nodes[location].connected_nodes}')

    destination = input('Enter your destination node (n1-n23): ')
    print(f'Ending node: {map_nodes[destination].node_id}')
    print(f'Ending Coordinates: {map_nodes[destination].node_pos}')
    print(f'Connected Nodes: {map_nodes[destination].connected_nodes}')

    path = get_path(map_nodes[location], map_nodes[destination], map_nodes)
    print(f'Path is: {path}')


if __name__ == '__main__':
    try:
        main()
    except  Exception as e:
        print(e)
        raise
