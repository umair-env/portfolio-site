# Umair Khan - Personal Portfolio Website

A modern, responsive personal portfolio website built with HTML, CSS, JavaScript, and optional Python Flask backend.

## 🚀 Features

- **Modern Design**: Clean, professional layout with dark/light theme toggle
- **Responsive**: Mobile-first design that works on all devices
- **Interactive**: Smooth animations, hover effects, and scroll animations
- **Contact Form**: Functional contact form with validation
- **Performance**: Optimized for fast loading and smooth interactions
- **Accessibility**: Semantic HTML and keyboard navigation support

## 🛠️ Technologies Used

### Frontend
- **HTML5**: Semantic markup structure
- **CSS3**: Modern styling with CSS Grid and Flexbox
- **JavaScript (ES6+)**: Interactive functionality and animations
- **AOS.js**: Animate On Scroll library for smooth animations
- **Font Awesome**: Icons for social media and UI elements
- **Google Fonts**: Inter font family for typography

### Backend (Optional)
- **Python Flask**: Lightweight web framework
- **Flask-CORS**: Cross-origin resource sharing
- **SMTP**: Email functionality for contact form

## 📁 Project Structure

```
portfolio/
├── index.html          # Main HTML file
├── style.css           # CSS styles and responsive design
├── script.js           # JavaScript functionality
├── app.py              # Flask backend (optional)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## 🚀 Getting Started

### Frontend Only (Recommended for most users)

1. **Clone or download** the project files
2. **Open** `index.html` in your web browser
3. **Customize** the content in `index.html` with your information
4. **Deploy** to any static hosting service (GitHub Pages, Netlify, Vercel, etc.)

### With Backend (For contact form functionality)

1. **Install Python** (3.7 or higher)
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables** (create a `.env` file):
   ```
   EMAIL_ADDRESS=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SECRET_KEY=your-secret-key
   ```
4. **Run the Flask server**:
   ```bash
   python app.py
   ```
5. **Open** `http://localhost:5000` in your browser

## 🎨 Customization

### Personal Information
Edit the following sections in `index.html`:
- Hero section: Name, title, description
- About section: Your story and experience
- Skills section: Your technical skills
- Projects section: Your portfolio projects
- Contact section: Your contact information

### Styling
Modify `style.css` to:
- Change color scheme in CSS variables
- Adjust typography and spacing
- Customize animations and transitions
- Add your own branding elements

### Functionality
Update `script.js` to:
- Add new interactive features
- Modify form validation
- Customize animations
- Add new JavaScript functionality

## 📱 Responsive Design

The website is fully responsive with breakpoints for:
- **Mobile**: 320px - 768px
- **Tablet**: 768px - 1024px
- **Desktop**: 1024px+

## 🌙 Theme Support

- **Light Theme**: Clean, professional appearance
- **Dark Theme**: Modern, eye-friendly dark mode
- **Auto-save**: Theme preference is saved in localStorage
- **Smooth Transitions**: Animated theme switching

## 📧 Contact Form

The contact form includes:
- **Client-side validation**: Real-time form validation
- **Server-side processing**: Flask backend for email sending
- **Success/Error notifications**: User feedback system
- **Spam protection**: Basic validation and rate limiting

## 🚀 Deployment

### Static Hosting (Frontend Only)
- **GitHub Pages**: Free hosting for static sites
- **Netlify**: Easy deployment with form handling
- **Vercel**: Fast global CDN
- **GitHub Pages**: Simple and free

### Full Stack Deployment
- **Heroku**: Easy Python deployment
- **DigitalOcean**: VPS hosting
- **AWS**: Scalable cloud hosting
- **Railway**: Modern deployment platform

## 🔧 Development

### Local Development
1. **Frontend**: Open `index.html` in browser
2. **Backend**: Run `python app.py` for Flask server
3. **Live Reload**: Use VS Code Live Server extension

### Browser Support
- **Modern Browsers**: Chrome, Firefox, Safari, Edge
- **Mobile Browsers**: iOS Safari, Chrome Mobile
- **Progressive Enhancement**: Works without JavaScript

## 📈 Performance

- **Optimized Images**: Placeholder system for fast loading
- **Minified Assets**: Compressed CSS and JavaScript
- **Lazy Loading**: Images load as needed
- **Smooth Animations**: 60fps animations with CSS transforms

## 🛡️ Security

- **Form Validation**: Client and server-side validation
- **CORS Protection**: Configured for production
- **Input Sanitization**: XSS prevention
- **Rate Limiting**: Contact form spam protection

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Umair Khan**
- GitHub: [@umair-env](https://github.com/umair-env)
- LinkedIn: [Umair Khan](https://www.linkedin.com/feed/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

If you have any questions or need help customizing this portfolio:
- Create an issue on GitHub
- Contact me through the portfolio contact form
- Email: umairkhan786ukz786@gmail.com

---

**Built with ❤️ by Umair Khan**
<br>
**Built using 🧠 obviously**
