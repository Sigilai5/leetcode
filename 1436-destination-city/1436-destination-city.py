class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        origin = []
        for path in paths:
            origin.append(path[0])
        for path in paths:
            if path[-1] not in origin:
                return path[1]
        