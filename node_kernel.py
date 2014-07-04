

from IPython.kernel.zmq.kernelbase import Kernel

class NodeKernel(Kernel):

    implementation = "node-kernel"
    implementation_version = "test"
    language = "javascript"
    language_version = "test"
    banner = "test"

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        if not silent:
            stream_content = {'name': 'stdout', 'data':'hi!'}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok', 'execution_count': self.execution_count,
                'payload': [], 'user_expressions': {}}

if __name__ == '__main__':
    from IPython.kernel.zmq.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=NodeKernel)
