from concurrent import futures

from tqdm import tqdm

from flags import get_flag, save_flag, show, main

MAX_WORKERS = 20

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower())
    
    return cc

def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        #res = executor.map(download_one, sorted(cc_list))
        to_do_map = {}
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do_map[future] = cc
        
        done_iter = futures.as_completed(to_do_map)
        done_iter = tqdm(done_iter, total=len(cc_list))
        for future in done_iter:
            res = future.result()
            #print(res)
    return len(cc_list)

if __name__ == '__main__':
    main(download_many)