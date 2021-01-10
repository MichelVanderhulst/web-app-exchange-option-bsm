import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64

bg_color="#506784",
font_color="#F3F6FA"

def header():
	return html.Div(
                id='app-page-header',
                children=[#html.Div(html.A(
		              #            id='lsm-logo', 
		              #            children=[html.Img(src='data:image/png;base64,{}'.format(base64.b64encode(open("output-onlinepngtools (1).png", 'rb').read()).decode()))],
		              #            href="https://uclouvain.be/en/faculties/lsm",
		              #            target="_blank", #open link in new tab
		              #            style={'margin':'20px'}
		              #              ), style={"display":"inline-block"}),
                    #
                    #
                    # html.Div(
	                   #  html.A(
	                   #  	id="nova-logo", 
	                   #  	children=[html.Img(src="data:image/png;base64,{}".format(base64.b64encode(open("output-onlinepngtools (2).png",'rb').read()).decode()))],
	                   #  	href="https://www2.novasbe.unl.pt/en/",
	                   #  	style={"margin":"-45px"}
	                   #  	  ), style={"display":"inline-block"}),
                    #
                    #
                    html.Div(children=[html.H3("Exchange option replication strategy app"),
                    				   html.H4("Black-Scholes-Merton model")
                    				  ],
                       		 style={"display":"inline-block", "font-family":'sans-serif'}),
                    #
                    #
                    html.Div(children=[dbc.Button("About", id="popover-target", outline=True, style={"color":"white", 'border': 'solid 1px white'}),
                    	      		   dbc.Popover(children=[dbc.PopoverHeader("About"),
                    	      	       		   	             dbc.PopoverBody(["Michel Vanderhulst",                     	    
                    	      	       		   	             				  "michelvanderhulst@student.uclouvain.be",
                    	      	       		   	             				  html.Hr(), 
                    	      	       		   	             				  "This app was built for my Master's Thesis, under the supervision of Prof. Frédéric Vrins (frederic.vrins@uclouvain.be)."
                    	      	       		   	             				  ],
                    	      	       		   	             				  #style={'padding':5}
                    	      	       		   	             				  ),
                    	      	       		   	             ],
                    	      	          		   id="popover",
                    	      	          		   #style={'width':'280px'},#,'height':'275px'},
                    	      	          		   is_open=False,
                    	      	          		   target="popover-target"),
                    	      		   ],
                    	      style={"display":"inline-block", "font-family":"sans-serif", 'marginLeft': '60%'}),
                		 ],
                style={
                    'background': bg_color,
                    'color': font_color,
                    'padding':20,
                    'margin':'-10px',
                }
            )
