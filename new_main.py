class Page:
    def home(self):
        boy = 1
        gal = 2
        x, y, z = self.logout()
        return x, y, z

    def logout(self):
        outside= 'Yes'
        inside= 'No'
        back= False
        return outside, inside, back


obj = Page()

x_value, y_value, z_value = obj.home()

a, b, c =Page.logout(True)

print(b)



print(x_value)