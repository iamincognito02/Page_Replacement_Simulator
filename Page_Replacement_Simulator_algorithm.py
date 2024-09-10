class PageReplacementAlgorithm:
    def __init__(self, frame_count):
        self.frame_count = frame_count
        self.frames = []

    def page_in(self, page, access_pattern):
        # Implement the page-in logic in the specific algorithm subclass
        pass

class FIFOPageReplacement(PageReplacementAlgorithm):
    def page_in(self, page, access_pattern):
        page_fault = 0
        eviction = 0
        replacement = 0

        if page not in self.frames:
            page_fault = 1

            if len(self.frames) < self.frame_count:
                self.frames.append(page)
            else:
                eviction = 1
                self.frames.pop(0)
                self.frames.append(page)
                replacement = 1

        return page_fault, eviction, replacement

class LRUPageReplacement(PageReplacementAlgorithm):
    def page_in(self, page, access_pattern):
        page_fault = 0
        eviction = 0
        replacement = 0

        if page not in self.frames:
            page_fault = 1

            if len(self.frames) >= self.frame_count:
                eviction = 1
                # Find and remove the least recently used page
                lru_page_index = self.find_lru_page(access_pattern)
                lru_page = self.frames.pop(lru_page_index)
            
            self.frames.append(page)

        return page_fault, eviction, replacement

    def find_lru_page(self, access_pattern):
        lru_index = -1
        lru_page = None

        for i, frame in enumerate(self.frames):
            if frame in access_pattern:
                index = access_pattern.index(frame)
                if index > lru_index:
                    lru_index = index
                    lru_page = frame

        return self.frames.index(lru_page)

class OPTPageReplacement(PageReplacementAlgorithm):
    def page_in(self, page, access_pattern):
        page_fault = 0
        eviction = 0
        replacement = 0

        if page not in self.frames:
            page_fault = 1

            if len(self.frames) >= self.frame_count:
                eviction = 1
                # Find the page in the frames that won't be used for the longest time (Optimal replacement)
                farthest_used = -1
                page_to_replace = None
                for i, frame in enumerate(self.frames):
                    if frame not in access_pattern[i:]:
                        page_to_replace = frame
                        break
                    distance = access_pattern[i:].index(frame)
                    if distance > farthest_used:
                        farthest_used = distance
                        page_to_replace = frame

                self.frames.remove(page_to_replace)
            self.frames.append(page)

        return page_fault, eviction, replacement
