    def animate_old(self, trajectory):

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        camera = Camera(fig)

        for pos in trajectory:

            x = trajectory
            b = -a

            # Initial values
            last_point = self.t_n[0]
            current_point = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
            last_xyz = [0,0,0]

            # Plotting data
            for i in (range(len(self.t_n))):

                ax.plot([x], [y], [z], marker=".", markersize=13, label='test point', color="grey", zorder=10) # plot joint

                current_point = mm(last_point, current_point)

                f = sym.lambdify(self.variables, current_point[0][3], "numpy") # define function x = f(variables)
                x = f(a, b) # calcualte x

                g = sym.lambdify(self.variables, current_point[1][3], "numpy") # define function y = g(variables)
                y = g(a, b) # calculate y

                h = sym.lambdify(self.variables, current_point[2][3], "numpy") # define function z = h(variables)
                z = h(a, b) # calculate z

                ax.plot([last_xyz[0], x], [last_xyz[1], y], [last_xyz[2], z], color="black", zorder=1) # plot link

                last_point = current_point
                if i != (len(self.t_n)-1):
                    current_point = self.t_n[i+1]
                last_xyz = [x,y,z]

            camera.snap()

        anim = camera.animate(interval=50, blit=True)
        anim.save('media/robot_01.gif', writer='imagemagick')
