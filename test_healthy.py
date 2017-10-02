from __future__ import print_function
from __future__ import unicode_literals
import sys
import logging
from pprint import pprint

from kazoo.client import KazooClient

from solrzkutil.healthy import (check_ephemeral_sessions_fast, 
                                check_ephemeral_dump_consistency, 
                                check_zookeeper_connectivity, 
                                check_ephemeral_znode_consistency,
                                get_solr_session_ids,
                                check_watch_sessions_duplicate,
                                check_watch_session_consistency,
                                check_watch_sessions_clients,
                                check_queue_sizes,
                                check_watch_sessions_valid,
                                check_overseer_election)

logging.basicConfig()
log = logging.getLogger()
kazoo_log = logging.getLogger('kazoo.client')
kazoo_log.setLevel(logging.INFO)
log.setLevel(logging.DEBUG)
zookeepers='zk01.host.com,zk02.host.com,zk03.host.com'
c = KazooClient(zookeepers)
print("ZK HOSTS: ", c.hosts)

def test_check_zookeeper_connectivity():
    response = check_zookeeper_connectivity(c)
    pprint(response)
    if not response:
        log.info('"check_zookeeper_connectivity" returned success!')
        
def test_check_ephemeral_sessions_fast():
    response = check_ephemeral_sessions_fast(c)
    pprint(response)
    if not response:
        log.info('"check_ephemeral_sessions_fast" returned success!')
        
def test_check_ephemeral_dump_consistency():
    response = check_ephemeral_dump_consistency(c)
    pprint(response)
    if not response:
        log.info('"check_ephemeral_dump_consistency" returned success!')
       
def test_check_ephemeral_znode_consistency():
    response = check_ephemeral_znode_consistency(c)
    pprint(response)
    if not response:
        log.info('"check_ephemeral_znode_consistency" returned success!')
        
def test_get_solr_session_ids():
    response = get_solr_session_ids(c)
    pprint(response)
    if response:
        log.info('"test_get_solr_session_ids" returned success!')

def test_check_watch_sessions_duplicate():
    response = check_watch_sessions_duplicate(c)
    pprint(response)
    if not response:
        log.info('"check_watch_sessions_duplicate" returned success!')

def test_check_watch_sessions_clients():
    response = check_watch_sessions_clients(c)
    pprint(response)
    if not response:
        log.info('"check_watch_session_clients" returned success!')

def test_check_queue_sizes():
    response = check_queue_sizes(c)
    pprint(response)
    if not response:
        log.info('"check_queue_sizes" returned success!')

def test_check_watch_sessions_valid():
    response = check_watch_sessions_valid(c)
    pprint(response)
    if not response:
        log.info('"check_watch_sessions_valid" returned success!')

def test_check_overseer_election():
    response = check_overseer_election(c)
    pprint(response)
    if not response:
        log.info('"check_overseer_election" returned success!')

def main(argv=None):
    test_check_zookeeper_connectivity()
    test_check_ephemeral_sessions_fast()
    test_check_ephemeral_znode_consistency()
    test_check_ephemeral_dump_consistency()
    test_get_solr_session_ids()
    test_check_watch_sessions_clients()
    test_check_watch_sessions_duplicate()
    test_check_queue_sizes()
    test_check_watch_sessions_valid()
    test_check_overseer_election()
    
if __name__ == '__main__':
    sys.exit(main())